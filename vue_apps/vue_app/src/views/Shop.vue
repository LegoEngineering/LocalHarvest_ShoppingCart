<template>
  <div class="shoponline">
    <div v-for="(item, index) in items" v-bind:key="item._id"> 
      <Card 
      :item = item 
      cardButtonText="Add to Cart"
      @cardButtonEvent="addProductToCart(index)"/>
    </div>
  </div>

</template>

<script>
import axios from "axios";
import Card from '@/components/Card.vue';
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
  },
  components: {
    Card
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