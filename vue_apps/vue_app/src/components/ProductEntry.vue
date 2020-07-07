<template>
  <div id="ProductEntry">
    <h1>{{ addHeaderText }}</h1>
    <h1>{{ searchHeaderText }}</h1>

    <input type="text" name="productname" v-model="input.productname" placeholder="Product Name" />
    <br>
    <input type="text" name= "productweight" v-model="input.productweight" placeholder="Product Weight" />
    <br>
    <input type="text" name= "productprice" v-model="input.productprice" placeholder="Product Price" />
    <br>
    <input type="text" name= "productsupply" v-model="input.productsupply" placeholder="Supply Amount" />
    <br>
    <b-form-group label="Add Tags to Product:">
      <b-form-checkbox-group
        id="checkbox-group-1"
        v-model="input.selected"
        :options="options"
        name="flavour-1"
      ></b-form-checkbox-group>
    </b-form-group>
    <button v-if="includeAddButton==true" type="button" @click="addsubmit">{{ addButtonText }}</button>
    <button v-if="includeSearchButton==true" type="button" @click="searchsubmit">{{ searchButtonText }}</button>
  </div>
</template>

<script>
export default {
  name: "ProductEntry",
  data() {
    return {
      input: {
        productname: "",
        productweight: "",
        productprice: "",
        productsupply: "",
        selected: []
      },
      options: []
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

    },
    modifysubmit() {
      console.log(this.input)
      this.$emit("modifySubmitEvent", this.input);
    }
  },
  props: {
    includeAddButton: Boolean,
    addButtonText: String,
    includeSearchButton: Boolean,
    searchButtonText: String,
  },
  mounted() {
    this.options = [
      { text: 'Orange', value: 'orange' },
      { text: 'Apple', value: 'apple' },
      { text: 'Pineapple', value: 'pineapple' },
      { text: 'Grape', value: 'grape' }
    ]
  },
};
</script>