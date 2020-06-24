<template>
  <div class="sidebar">
    <b-button variant="light" v-b-toggle.sidebar-right>
      <b-icon-cart2></b-icon-cart2> 
    </b-button>
    <b-sidebar id="sidebar-right" title="My Cart" right shadow>
      <div class="px-3 py-2" v-for="(item) in items" v-bind:key="item._id">
          <div>
            {{item.product.productname}}
            {{item.quantity}}
          </div>
      </div>
    </b-sidebar>
  </div>
</template>

<script>
import axios from "axios";
import Shop from '@/views/Shop.vue';
import { EventBus } from '@/event-bus.js';
export default {
  name: "sidebar",
  data() {
    return {
      message: "",
      items: []
    }
  },  
  components: {
    Shop
  },
  mounted() {
    EventBus.$on('addProductToCartEvent', (newCartItem) => {
      if (this.items.some(item => item.product === newCartItem)){
        item.quantity++
        console.log(item);    
        console.log(quantity);    
      } else {
        var quantity = 1
        this.items.push({"product": newCartItem, "quantity": quantity});
      }
    });
  }
}
</script>

<style scoped>
.sidebar {
  float: right;
  }
</style>