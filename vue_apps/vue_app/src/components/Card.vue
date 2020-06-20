<template>
    <b-card order-variant="light" class="card" id="productcard">
      
        <div>{{item.productname}}</div>
        <div>{{item.productweight}}</div>
        <div>{{item.productprice}}</div>
        <div>{{item.productsupply}}</div>

        <button type="button" @click="cardbutton">{{ cardButtonText }}</button> 
    </b-card>
</template>

<script>
export default {
  name: 'card',
  props: {
    item: {},
    cardButtonText: String
  },
  methods: {
    cardbutton() {
      console.log(this.item)
      this.$emit("cardButtonEvent");
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