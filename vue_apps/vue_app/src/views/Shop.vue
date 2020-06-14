<template>
  <div>
    <div class="productcard" v-for="(item, index) in items" v-bind:key="item._id">
        {{item.productname}}
        <button type="button" @click="addProductToCart(index)">Add to Cart</button>

          
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
.productcard {
  border: 1px solid #000000;
  background-color: #a89f9f;
  margin: auto;
  margin-top: 200px;
  padding: 20px;
  }

</style>