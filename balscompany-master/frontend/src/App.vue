<template>
  <v-app class="overflow-auto" style="
        width: 100%;
        height: 100%;
        padding: 0px;
        margin: 0px;
        overflow-x: hidden;">
    <HeaderComponent class="header" style="max-width: 100%"></HeaderComponent>
    <v-main>
      <router-view />
    </v-main>
    <FooterComponent class="footer"></FooterComponent>
  </v-app>
</template>

<script>
import HeaderComponent from "@/components/HeaderComponent.vue";
import FooterComponent from "@/components/FooterComponent.vue";

export default {
  name: "App",
  components: { HeaderComponent, FooterComponent },
};
</script>

<style>
* {
  transition-duration: 250ms;
  transition-property: transform;
}
.hoverable:hover {
  z-index: 999 !important;
}
.header,
.footer {
  z-index: 1000 !important;
}
</style>