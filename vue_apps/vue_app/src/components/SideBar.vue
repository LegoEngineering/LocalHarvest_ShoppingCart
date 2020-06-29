<template>
  <div class="sidebar">
    <b-button variant="light" v-b-toggle.sidebar-right>
      <b-icon-cart2></b-icon-cart2> 
    </b-button>
    <b-sidebar id="sidebar-right" title="My Cart" right shadow>
      <div class="px-3 py-2">
          <div>
            <b-table striped hover :fields="fields" :items="items" v-bind:key="tableVersion">
            <template v-slot:cell()="data">{{ data.value }}</template>
          </div>
          <button v-if="items[0]" type="button" @click="checkoutCart">Checkout</button>
          <button v-if="items[0]" type="button" @click="viewCart">View Cart</button>
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
        { key: "product.productname", label:""},
        { key: "quantity", label:""},
        { key: "product.productprice", label:""}
      ],
      message: "",
      items: [],
      tableVersion: 0
    }
  },  
  components: {
    Shop
  },
  methods: {
    checkoutCart: async function(items) {
      console.log(this.items)
      const carto = {"cartitems": this.items}
      try {
        let result = await axios.post("/api/cart", carto);
        console.log(result)
        this.message = result.data.message
      } catch (e) {
        if (e.response.data.message) {
          this.message = e.response.data.message;
        } else {
          this.message = "Unable to checkout at this time";
        }
      }
    },
    viewCart: async function() {
      try {
        let getresult = await axios.get("/api/cart");
        console.log(getresult)
        //this.message = result.data.message
      } catch (e) {
        if (e.response.data.message) {
          this.message = e.response.data.message;
        } else {
          this.message = "Unable to retrieve at this time";
        }
      }
    }  
  },

  mounted() {
    EventBus.$on('addProductToCart', (cartItemIncludeValue) => {
        this.items.push({"product": cartItemIncludeValue.cartItem, "quantity": cartItemIncludeValue.quantity});
    }),
    EventBus.$on('changeProductQuantity', (cartItemIncludeValue) => {
        const i = this.items.findIndex(item => cartItemIncludeValue.cartItem===item.product)
        this.items[i].quantity=cartItemIncludeValue.quantity
    }),
    EventBus.$on('removeProductFromCart', (cartItemIncludeValue) => {
        const i = this.items.findIndex(item => cartItemIncludeValue.cartItem===item.product)
        if (i > -1) {
          this.items.splice(i, 1);
        }
        this.tableVersion++
    });

  }
}
</script>

<style scoped>
.sidebar {
  float: right;
  }
</style>