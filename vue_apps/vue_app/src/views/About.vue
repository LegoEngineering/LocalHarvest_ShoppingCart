
<template>
  <div class="about">
    <h1>This is an about page</h1>
    <Card :item = item />
  </div>
</template>

<script>
import Card from '@/components/Card.vue'

export default {
  name: 'about',
  data(){
    return {
      item: { 
      productname: "scadsfaz",
      productweight: "asdkj",
      productprice: "sdkag", 
      productsupply: "asdnv" }
    }
  },
  components: {
    Card
  }
}
</script>