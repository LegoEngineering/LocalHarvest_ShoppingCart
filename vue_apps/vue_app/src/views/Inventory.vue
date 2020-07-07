<template>
<div>
    <manageProducts />
</div>
</template>


<script>
import manageProducts from "@/components/manageProducts.vue";
export default {
  name: "Inventory",
  data() {
    return {
      inventoryVersion: 0
    };
  },
  components: {
    ProductEntry
  },
  methods: {

  },
  mounted() {
    EventBus.$on('shopInventoryUpdate', () => {
      this.inventoryVersion++
    })
  }
  };
</script>