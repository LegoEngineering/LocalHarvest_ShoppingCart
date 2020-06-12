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
  </div>
</template>


<script>
import axios from "axios";
import InventoryEvents from "@/components/InventoryEvents.vue";
export default {
  name: "inventory",
  data() {
    return {
      message: ""
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
     console.log(input)
      try {
        let result = await axios.get("/api/product", {params: {Scribbles: input}, headers:{}})
        this.message = result.data.value
        console.log(result)
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