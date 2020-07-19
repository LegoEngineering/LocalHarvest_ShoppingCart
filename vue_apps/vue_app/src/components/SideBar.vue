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
          <div v-bind:key="tableVersion">${{sumItemCosts}} USD</div>
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
      tableVersion: 0,
      temp: {}
    }
  },  
  components: {
    Shop
  },
  methods: {
    checkoutCart: async function(items) {
      console.log(this.items)
      const cart = {"cartitems": this.items}
      try {
        let result = await axios.post("/api/cart", cart);
        console.log(result)
        this.message = result.data.message
        this.$router.push("/Checkout");
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
      this.temp = JSON.parse(localStorage.getItem('tempCart'));
      console.log(this.temp)
      //this.totalcost =this.temp.tempTotalCost
      //this.items = this.temp.tempItems
    }

    EventBus.$on('addProductToCart', (cartItemIncludeQuantity) => {
        this.items.push({"product": cartItemIncludeQuantity.cartItem, "quantity": cartItemIncludeQuantity.quantity, "itemTotalCost": parseFloat(cartItemIncludeQuantity.cartItem.productprice)});
        this.tableVersion++
        localStorage.setItem('tempCart', JSON.stringify({"tempItems":this.items,"tempTotalCost":this.sumItemCosts}));  
    }),
    EventBus.$on('changeProductQuantity', (cartItemIncludeQuantity) => {
        const i = this.items.findIndex(item => cartItemIncludeQuantity.cartItem===item.product)
        this.items[i].quantity=cartItemIncludeQuantity.quantity
        this.items[i].itemTotalCost= cartItemIncludeQuantity.quantity*parseFloat(cartItemIncludeQuantity.cartItem.productprice).toFixed(2)
        console.log(this.items[i].itemTotalCost)
        this.tableVersion++
        localStorage.setItem('tempCart', JSON.stringify({"tempItems":this.items,"tempTotalCost":this.sumItemCosts}));  
    }),
    EventBus.$on('removeProductFromCart', (cartItemIncludeQuantity) => {
        const i = this.items.findIndex(item => cartItemIncludeQuantity.cartItem===item.product)
        if (i > -1) {
          this.items.splice(i, 1);
        }
        this.tableVersion++
        localStorage.setItem('tempCart', JSON.stringify({"tempItems":this.items,"tempTotalCost":this.sumItemCosts}));  
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