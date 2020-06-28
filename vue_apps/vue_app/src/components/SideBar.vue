<template>
  <div class="sidebar">
    <b-button variant="light" v-b-toggle.sidebar-right>
      <b-icon-cart2></b-icon-cart2> 
    </b-button>
    <b-sidebar id="sidebar-right" title="My Cart" right shadow>
      <div class="px-3 py-2" v-for="(item) in items" v-bind:key="item._id">
          <div>
            <b-table striped hover :fields="fields" :items="items">
            <template v-slot:cell()="data">{{ data.item }}</template>
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
      fields: [
        { key: "product.productname", label: "productname" },
        { key: "product.quantity", label: "quantity" },
        { key: "product.productprice", label: "productprice" }
      ],
      message: "",
      items: []
    }
  },  
  components: {
    Shop
  },
  mounted() {
    EventBus.$on('addProductToCart', (cartItemIncludeValue) => {
      console.log(cartItemIncludeValue)
        this.items.push({"product": cartItemIncludeValue.cartItem, "quantity": cartItemIncludeValue.quantity});
    }),
    EventBus.$on('changeProductQuantity', (cartItemIncludeValue) => {
      console.log(cartItemIncludeValue)
        const i = this.items.findIndex(item => cartItemIncludeValue.cartItem===item.product)
          console.log(i)
          console.log(cartItemIncludeValue.cartItem)
        this.items[i].quantity=cartItemIncludeValue.quantity
    });
  }
}
</script>

<style scoped>
.sidebar {
  float: right;
  }
</style>