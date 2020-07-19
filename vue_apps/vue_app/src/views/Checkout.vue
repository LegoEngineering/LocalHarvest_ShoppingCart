<template>
  <div class="checkout">
    <div v-if="!paidFor">
      <div>
        <b-table striped hover :fields="fields" :items="items">
        <template v-slot:cell()="data">{{ data.value }}</template>
      </div>
      <div>
        ${{totalcost}} USD
      </div>
    </div>

    <div v-if="paidFor">
      <h3>Order has been completed! Order #</h3>
    </div>

    <div ref="paypal"></div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "checkout",

  data: function() {
    return {
      loaded: false,
      paidFor: false,
      items: [],
      fields: [
        { key: "product.productname", label:""},
        { key: "quantity", label:""},
        { key: "itemTotalCost", label:""}
      ],
      totalcost: 0
    };
  },
  mounted: function() {
    const script = document.createElement("script");
    script.src =
      "https://www.paypal.com/sdk/js?client-id=AXe9_ewDIAZnTQEsSEIKl85Nn-3n7RiYT0FkYrDeDFBNG-qsEU1_pBm6zvWYTB158zyyoe7spNl-bLGL";
    script.addEventListener("load", this.setLoaded);
    document.body.appendChild(script);
    if(!localStorage.getItem('tempCart')){
      console.log('no such cart')
    } else {
      let tempCart = JSON.parse(localStorage.getItem('tempCart'));
      this.items = tempCart.tempItems
      this.totalcost = tempCart.tempTotalCost
    }
  },
  methods: {
    setLoaded: function() {
      this.loaded = true;
      window.paypal
        .Buttons({
          createOrder: (data, actions) => {
            return actions.order.create({
              purchase_units: [
                {
                  description: "Local Harvest cart",
                  amount: {
                    currency_code: "USD",
                    value: this.totalcost
                  }
                }
              ]
            });
          },
          onApprove: async (data, actions) => {
            const order = await actions.order.capture();
            this.paidFor = true;
            console.log(order);
          },
          onError: err => {
            console.log(err);
          }
        })
        .render(this.$refs.paypal);
    }
  }
};
</script>