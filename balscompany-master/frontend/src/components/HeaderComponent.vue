<template>
  <v-app-bar height="70" app>
    <v-img @click="gotoHome()" style="cursor:pointer" contain src="@/assets/logo-header.webp" max-width="100"></v-img>
    <v-tabs class="ps-5">
      <v-tab to="/">Inicio</v-tab>
      <v-tab to="/trabaja-con-nosotros">Trabaja con nosotros</v-tab>
      <v-tab to="/info">¿Quiénes somos?</v-tab>
    </v-tabs>
    
  </v-app-bar>
</template>
  
<script>

export default {
  name: "HeaderComponent",
  data() {
    return {
    }
  },
  methods:{
    gotoHome(){
      this.$router.push('/').catch(() => {});
    }
  }
};
</script>
<style scoped>
.v-tab{
  font-size: .7em;
}
</style>