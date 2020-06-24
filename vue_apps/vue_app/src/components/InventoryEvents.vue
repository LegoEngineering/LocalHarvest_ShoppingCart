<template>
  <div id="inventoryevents">
    <h1>{{ addHeaderText }}</h1>
    <h1>{{ searchHeaderText }}</h1>

    <input type="text" name="productname" v-model="input.productname" placeholder="Product Name" />
    <input type="text" name= "productweight" v-model="input.productweight" placeholder="Product Weight" />
    <input type="text" name= "productprice" v-model="input.productprice" placeholder="Product Price" />
    <input type="text" name= "productsupply" v-model="input.productsupply" placeholder="Supply Amount" />
    <button type="button" @click="addsubmit">{{ addButtonText }}</button>
    <button type="button" @click="searchsubmit">{{ searchButtonText }}</button>
  </div>
</template>

<script>
export default {
  name: "InventoryEvents",
  data() {
    return {
      input: {
        productname: "",
        productweight: "",
        productprice: "",
        productsupply: "",
      }
    };
  },
  methods: {
    addsubmit() {
      console.log(this.input)
      this.$emit("addSubmitEvent", this.input);
    },
    searchsubmit() {
      console.log(this.input)
      this.$emit("searchSubmitEvent", this.input);
    }
    },
  props: {
    addButtonText: String,
    addHeaderText: String,
    searchButtonText: String,
    searchHeaderText: String
  }
};
</script>