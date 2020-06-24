<template>
    <div class="searchbar">
        <input type="text" name="productname" v-model="input.productname" placeholder="Product Name" />
        <input type="text" name= "productweight" v-model="input.productweight" placeholder="Product Weight" />
        <input type="text" name= "productprice" v-model="input.productprice" placeholder="Product Price" />
        <input type="text" name= "productsupply" v-model="input.productsupply" placeholder="Supply Amount" />
        <button type="button" @click="searchProduct(input)">Search</button>

    </div>
</template>

<script>
import axios from "axios";
export default {
  name: 'SearchBar',
  data() {
    return {
      input: {
        productname: "",
        productweight: "",
        productprice: "",
        productsupply: "",
      },
      message: "",
      searchResult: []
    };
  },
  methods: {
    searchProduct: async function(input) {
        try {
        let result = await axios.get("/api/product", {params: {productname: input.productname}, headers:{}})
        console.log(result)
        this.message = result.data
        this.searchResult = result.data
        this.$emit("searchSubmitEvent", this.searchResult)
      } catch (e) {
        if (e.response.data.message) {
          this.message = e.response.data.message;
        } else {
          this.message = "Unable to search for a product at this time";
        }
      }
    }
  }
}
</script>