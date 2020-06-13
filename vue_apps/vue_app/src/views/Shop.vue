<template>
<div id="shoponline">
  <ul>
    <li v-for="item in items" v-bind:key="item.productname">{{ item }}</li>
    <v-card max-width="400">
    </v-card>
  </ul>
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
      console.log("warning yo")
      try {
        let result = await axios.get("/api/product")
        this.productname = result.data.value
        this.items = result.data
        console.log(result)
      } catch (e) {
        if (e.response.data.message) {
          this.message = e.response.data.message;
        } else {
          this.message = "Unable to search for a product at this time";
        }
      }
    }
  },
  mounted() {
    this.getAllProducts();
  }
}
    
</script>

