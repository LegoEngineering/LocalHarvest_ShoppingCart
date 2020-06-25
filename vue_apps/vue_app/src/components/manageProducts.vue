<template>
  <div id="manageProducts">
    <ProductEntry
      includeAddButton = 1
      addButtonText="Add"
      @addSubmitEvent="addNewProduct"
      includeSearchButton= 1 
      searchButtonText="Search"
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
import ProductEntry from "@/components/ProductEntry.vue";
export default {
  name: "manageProducts",
  data() {
    return {
      message: "",
      items: [],
      searchResult: []
    };
  },
  components: {
    ProductEntry
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
        if (typeof result.data === 'string') {
          this.message = result.data
        } else {
          this.searchResult = result.data
          this.$emit("searchSubmitEvent", this.searchResult)
        }
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