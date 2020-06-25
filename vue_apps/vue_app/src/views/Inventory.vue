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
    };
  },
  components: {
    ProductEntry
  },
  methods: {}
  }
};
</script>