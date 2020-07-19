<template>
    <b-card order-variant="light" class="card" id="productcard">
      
        <div>{{item.productname}}</div>
        <div>{{item.productweight}}</div>
        <div>{{item.productprice}}</div>
        <div>{{item.productsupply}}</div>

        <label for="sb-inline">{{ cardButtonText }}</label>
        <b-form-spinbutton 
          id="sb-inline"
          v-model="quantity" 
          @change="cardbutton" 
          inline 
          min="0">
        </b-form-spinbutton>
    </b-card>
</template>

<script>
import { EventBus } from '@/event-bus.js';
export default {
  name: 'card',
  data() {
      return {
        quantity: 0,
        isAdded: 0,
      }
    },
  props: {
    item: {},
    cardButtonText: String
  },
  methods: {
    cardbutton() {
      if (this.quantity ==1) {
        if(this.isAdded ==0) {
          this.isAdded = 1
          EventBus.$emit("addProductToCart", {"cartItem": this.item, "quantity": this.quantity});
        } else {
          EventBus.$emit("changeProductQuantity", {"cartItem": this.item, "quantity": this.quantity});
        }
      } else if (this.quantity==0) {
          if(this.isAdded ==1) {
            this.isAdded = 0
            EventBus.$emit("removeProductFromCart", {"cartItem": this.item, "quantity": this.quantity});
          }
      } else {
        EventBus.$emit("changeProductQuantity", {"cartItem": this.item, "quantity": this.quantity});
      }
    }
  },
  mounted() {
        EventBus.$on('addProductToCart', (cartItemIncludeQuantity) => {
        if(cartItemIncludeQuantity.product == this.item) {
          this.quantity = cartItemIncludeQuantity.quantity
        }
        }),
        EventBus.$on('changeProductQuantity', (cartItemIncludeQuantity) => {
        if(cartItemIncludeQuantity.product == this.item) {
          this.quantity = cartItemIncludeQuantity.quantity
        }
        }),
        EventBus.$on('removeProductFromCart', (cartItemIncludeQuantity) => {
        if(cartItemIncludeQuantity.product == this.item) {
          this.quantity = cartItemIncludeQuantity.quantity
        }
        })
        EventBus.$on('getPastCartEvent', (cartItemIncludeQuantity) => {
        if(cartItemIncludeQuantity.cartItem == this.item) {
          this.quantity = cartItemIncludeQuantity.quantity
        }
        })
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
  text-align: center;
  }
</style>