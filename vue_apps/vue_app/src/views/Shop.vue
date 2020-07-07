<template>
  <div class="shoponline">
    <manageProducts purpose="searchBar" @searchSubmitEvent="displaySearchResults"/>
    <div v-bind:key="shopVersion">
      <div v-for="(item, index) in items" v-bind:key="item._id"> 
          <Card 
          :item = item 
          cardButtonText="Add to Cart"
          @addProductToCart="addToCart(index, $event)"
          @productQuantityIsOne= "changeQuantity(index, $event)"
          @removeProductFromCart = "changeQuantity(index, $event)"
          @changeProductQuantity = "changeQuantity(index, $event)"
          />
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
      shopVersion: 0
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
    addToCart: async function(index, value) {
      this.message = "Item has been added!"
      EventBus.$emit("addProductToCart", {"cartItem": this.items[index], "quantity": value});
    },
    changeQuantity: async function(index, value) {
      if(value != 0){
        EventBus.$emit("changeProductQuantity", {"cartItem": this.items[index], "quantity": value});
      } else {
        EventBus.$emit("removeProductFromCart", {"cartItem": this.items[index], "quantity": value});
      }
    },
    displaySearchResults: async function(searchResult) {
      this.items = searchResult
    },

  },
  mounted() {
    EventBus.$on('shopInventoryUpdate', () => {
        this.shopVersion++
        console.log("rerender should happen")
        console.log(this.shopVersion)
    })
    this.getAllProducts();
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