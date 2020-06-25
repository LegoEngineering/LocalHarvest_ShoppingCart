<template>
  <div class="shoponline">
    <manageProducts purpose="searchBar" @searchSubmitEvent="displaySearchResults" />
    <div v-for="(item, index) in items" v-bind:key="item._id"> 
      <Card 
      :item = item 
      cardButtonText="Add to Cart"
      @cardButtonEvent="addProductToCart(index)"/>
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
      items: []

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
    addProductToCart: async function(index) {
      this.message = "Item has been added!"
      var newCartItem = this.items[index]
      EventBus.$emit("addProductToCartEvent", newCartItem);
    },
    displaySearchResults: async function(searchResult) {
      this.items = searchResult
    }

  },
  mounted() {
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