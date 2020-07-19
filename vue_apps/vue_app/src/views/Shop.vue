<template>
  <div class="shoponline">
    <manageProducts purpose="searchBar" @searchSubmitEvent="displaySearchResults"/>
    <div v-bind:key="shopVersion">
      <div v-for="item in items" v-bind:key="item._id"> 
          <Card 
          :item = item 
          cardButtonText="Add to Cart"/>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import manageProducts from '@/components/manageProducts.vue';
import Card from '@/components/Card.vue';
import { EventBus } from '@/event-bus.js';
export default {
  name: "shoponline",
  data() {
    return {
      message: "",
      items: [],
      shopVersion: 0,
      cart: []
    }
  },
  methods: {
    getAllProducts: async function() {
      try {
        let result = await axios.get("/api/product")
        this.items= result.data
      } catch (e) {
        if (e.response.data.message) {
          this.message = e.response.data.message;
        } else {
          this.message = "Unable to display products at this time";
        }
      }
    },
    displaySearchResults: async function(searchResult) {
      this.items = searchResult
    },
    getPastCart: async function() {
      if(!localStorage.getItem('tempCart')){
      console.log('no such cart')
        } else {
      this.cart = JSON.parse(localStorage.getItem('tempCart'));
      this.cart.forEach(function(item) {
      EventBus.$emit("getPastCartEvent", {"cartItem": item.product, "quantity": item.quantity});
      });
    }
    }
  },
  mounted() {
    EventBus.$on('shopInventoryUpdate', () => {
        this.shopVersion++
        console.log("rerender should happen")
        console.log(this.shopVersion)
    })
    this.getAllProducts();
    //this.getPastCart();

  },
  components: {
    Card,
    manageProducts
  }
}
    
</script>

<style scoped>
#productcard {
  width: 200px;
  margin-left: 40px;
  margin-top: 20px;
  padding: 10px;
  float: left;
  }

</style>