<template>
  <div id="inventory">
    <InventoryEvents
      addHeaderText="Add Product"
      addButtonText="add"
      @addSubmitEvent="addNewProduct"
      searchHeaderText="Search for a Product"
      searchButtonText="search"
      @searchSubmitEvent="searchProduct"
    />
    <label>{{message}}</label>

  <ul>
    <li v-for="item in items" v-bind:key="item.productname">{{ item }}</li>
  <v-card max-width="400">
  
  </v-card>
  </ul>

  </div>
</template>


<script>
import axios from "axios";
import InventoryEvents from "@/components/InventoryEvents.vue";
export default {
  name: "inventory",
  data() {
    return {
      message: "",
      items: []
    };
  },
  components: {
    InventoryEvents
  },
  methods: {
    addNewProduct: async function(input) {
     console.log(input)
      try {
        let result = await axios.post("/api/product", input);

        this.message = result.data.message
      } catch (e) {
        if (e.response.data.message) {
          this.message = e.response.data.message;
        } else {
          this.message = "Unable to add a product at this time";
        }
      }
    },
    searchProduct: async function(input) {
      try {
        let result = await axios.get("/api/product", {params: {productname: input.productname}, headers:{}})
        console.log(result)
        this.message = result.data
        this.items = result.data
      } catch (e) {
        if (e.response.data.message) {
          this.message = e.response.data.message;
        } else {
          this.message = "Unable to search for a product at this time";
        }
      }
    }
  }
};
</script>