<template>
  <div>
    <div>
    <b-card order-variant="light" class="text-center" id="productcard" v-for="(item, index) in items" v-bind:key="item._id">
      
        <div>{{item.productname}}</div>
        <div>{{item.productweight}}</div>
        <div>{{item.productprice}}</div>
        <div>{{item.productsupply}}</div>

        <button type="button" @click="addProductToCart(index)">Add to Cart</button> 
    </b-card>
    </div>
  </div>

</template>

<script>
import axios from "axios";
export default {
  name: "shoponline",
  data() {
    return {
      message: "",
      items: []
    }
  },
  methods: {
    getAllProducts: async function() {
      try {
        let result = await axios.get("/api/product")
        this.items= result.data
        console.log(result)
      } catch (e) {
        if (e.response.data.message) {
          this.message = e.response.data.message;
        } else {
          this.message = "Unable to search for a product at this time";
        }
      }
    },
    addProductToCart: async function(index) {
      this.message = "Item has been added!"
      console.log(index)
      console.log(this.items[index])
    }

  },
  mounted() {
    this.getAllProducts();
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