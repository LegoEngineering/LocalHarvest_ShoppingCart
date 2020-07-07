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
          <div v-bind:key="tableVersion">{{sumItemCosts}}</div>
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
        { key: "itemTotalCost", label:""}
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
    if(!localStorage.getItem('tempCart')){
      console.log('no such cart')
    } else {
      this.items = JSON.parse(localStorage.getItem('tempCart'));
    }

    EventBus.$on('addProductToCart', (cartItemIncludeValue) => {
        this.items.push({"product": cartItemIncludeValue.cartItem, "quantity": cartItemIncludeValue.quantity, "itemTotalCost": parseFloat(cartItemIncludeValue.cartItem.productprice)});
        this.tableVersion++
        localStorage.setItem('tempCart', JSON.stringify(this.items));       

    }),
    EventBus.$on('changeProductQuantity', (cartItemIncludeValue) => {
        const i = this.items.findIndex(item => cartItemIncludeValue.cartItem===item.product)
        this.items[i].quantity=cartItemIncludeValue.quantity
        this.items[i].itemTotalCost= cartItemIncludeValue.quantity*parseFloat(cartItemIncludeValue.cartItem.productprice).toFixed(2)
        console.log(this.items[i].itemTotalCost)
        this.tableVersion++
        localStorage.setItem('tempCart', JSON.stringify(this.items)); 
    }),
    EventBus.$on('removeProductFromCart', (cartItemIncludeValue) => {
        const i = this.items.findIndex(item => cartItemIncludeValue.cartItem===item.product)
        if (i > -1) {
          this.items.splice(i, 1);
        }
        this.tableVersion++
        localStorage.setItem('tempCart', JSON.stringify(this.items)); 
    });

  },
  computed: {
    sumItemCosts: function(){
      let cartTotalCost = 0;
      this.items.forEach(function(item) {
        cartTotalCost += item.itemTotalCost;
        console.log(item)
      });
      console.log(cartTotalCost)
      return cartTotalCost;
   }
  }
}
</script>

<style scoped>
.sidebar {
  float: right;
  }
</style>