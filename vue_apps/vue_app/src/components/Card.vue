<template>
    <b-card order-variant="light" class="card" id="productcard">
      
        <div>{{item.productname}}</div>
        <div>{{item.productweight}}</div>
        <div>{{item.productprice}}</div>
        <div>{{item.productsupply}}</div>

        <label for="sb-inline">{{ cardButtonText }}</label>
        <b-form-spinbutton 
          id="sb-inline"
          v-model="value" 
          @change="cardbutton" 
          inline 
          min="0">
        </b-form-spinbutton>
    </b-card>
</template>

<script>
export default {
  name: 'card',
  data() {
      return {
        value: 0,
        isAdded: 0,
      }
    },
  props: {
    item: {},
    cardButtonText: String
  },
  methods: {
    cardbutton() {
      if (this.value ==1) {
        if(this.isAdded ==0) {
          this.isAdded = 1
          this.$emit("addProductToCart", this.value);
        } else {
          this.$emit("productQuantityIsOne", this.value);
        }
      } else if (this.value==0) {
          if(this.isAdded ==1) {
            this.isAdded = 0
            this.$emit("removeProductFromCart", this.value);
          }
      } else {
        this.$emit("changeProductQuantity", this.value);
    }
  }
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
  text-align: center;
  }
</style>