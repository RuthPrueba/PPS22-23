<template>
  <v-footer padless class="mt-10">
    <v-card
      flat
      tile
      width="100%"
      class="pt-5 text-center"
      style="background-color: var(--v-secondary-darken1)"
    >
      <v-row>
        <v-col cols="12" md="6">
          <div>
            <h3 style="color: var(--v-secondary-lighten5)">Contacto</h3>
            <div id="selectFooter">
              <v-select
                id="selectFooter"
                class="mx-auto my-2"
                color="primary"
                style="max-width:30%;"
                dense
                filled
                outlined
                hide-details
                :items="sedes"
                v-model="seleccionada"
                :item-value="(item) => item"
                :item-text="(item) => item.localidad"
              ></v-select>
            </div>
          </div>
          <p style="color: var(--v-secondary-lighten5)">
            {{ seleccionada.tlf }}
          </p>
          <p style="color: var(--v-secondary-lighten5)">
            {{ seleccionada.email }}
          </p>
          <p style="color: var(--v-secondary-lighten5)">
            {{ seleccionada.direccion }}
          </p>
          <p style="color: var(--v-secondary-lighten5)">
            {{ seleccionada.cp }}
          </p>
        </v-col>
        <v-col cols="12" md="6">
          <h3 style="color: var(--v-secondary-lighten5)">Redes sociales</h3>
          <p style="color: var(--v-secondary-lighten5)"></p>
        </v-col>
      </v-row>
      <v-divider></v-divider>
      <v-card-text style="color: var(--v-secondary-lighten5)">
        Copyright {{ new Date().getFullYear() }} —
        <strong>BalsCompany SL</strong>
      </v-card-text>
    </v-card>
  </v-footer>
</template>

<script>
export default {
  name: "FooterComponent",
  data() {
    return {
      sedes: [
        {
          localidad: "Murcia",
          direccion: "C/ Puerta Nueva, 12",
          tlf: "968 46 90 72",
          email: "murcia@balscompany.com",
          cp: "30001",
        },
        {
          localidad: "Villarrobledo",
          direccion: "C/ Cohete, 15",
          tlf: "967 37 46 60",
          email: "villarrobledo@balscompany.com",
          cp: "02600",
        },
        {
          localidad: "Albacete",
          direccion: "C/ Gracia, 10",
          tlf: "967 24 30 58",
          email: "albacete@balscompany.com",
          cp: "02005 ",
        },
        {
          localidad: "Madrid",
          direccion: "C/ Miosotis, 54",
          tlf: "919 37 50 40",
          email: "madrid@balscompany.com",
          cp: "28039",
        },
      ],
      seleccionada: {
        localidad: "Madrid",
        direccion: "C/ Miosotis, 54",
        tlf: "919 37 50 40",
        email: "madrid@balscompany.com",
        cp: "28039",
      },
    };
  },
};
</script>
<style>
#selectFooter .v-select.v-input--dense .v-select__selection--comma{
  color:var(--v-secondary-lighten5);
}
#selectFooter .v-select.theme--light.v-text-field--outlined:not(.v-input--is-focused):not(.v-input--has-state) > .v-input__control > .v-input__slot fieldset{
  border-color: var(--v-secondary-lighten5);
}
#selectFooter .v-select .mdi-menu-down::before,#selectFooter  .v-select .mdi-menu-up::before {
  color: var(--v-secondary-lighten5);
}
</style>