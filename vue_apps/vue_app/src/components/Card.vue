<template>
  <div class="card">
    <b-card order-variant="light" class="text-center" id="productcard">
      
        <div>{{item.productname}}</div>
        <div>{{item.productweight}}</div>
        <div>{{item.productprice}}</div>
        <div>{{item.productsupply}}</div>

        <button type="button">Add to Cart</button> 
    </b-card>
  </div>
</template>

<script>
export default {
  name: 'card',
  props: {
    item: {}
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