<template>
  <div>
    <v-img src="@/assets/logo.webp" width="45%" class="mx-auto my-15"></v-img>
    <v-row>
      <v-col cols="12" md="4" class="px-5 px-lg-15">
        <v-hover v-slot="{ hover }" >
          <v-card 
          style="cursor: pointer" 
          height="100%" 
          width="100%"
          :elevation="hover ? 12 : 2"
          >
            <v-card-title>Plan Base</v-card-title>
            <v-card-text>
              <ul>
                <li>2 toneladas de producto escogido cada trimestre</li>
                <li>
                  Descuentos en la tienda online dependiendo de la temporada
                </li>
                <li>Asistencia al cliente normal</li>
              </ul>
            </v-card-text>
            <div class="mt-5 cAction">
              <v-divider class="mx-4 mb-5"></v-divider>
              <strong
                class="text-h4 ms-5 font-weight-bold"
                style="color: var(--v-primary-base)"
              >
                119.99€ / 3 meses
                <br />
              </strong>
              <p class="text-h5 ms-7 font-weight-bold">(44.99 / mes)</p>
            </div>
          </v-card>
        </v-hover>
      </v-col>
      <v-col cols="12" md="4" class="px-5 px-lg-15">
        <v-hover v-slot="{ hover }" >
          <v-card
            style="cursor: pointer"
            height="100%"
            width="100%"
            class="d-flex flex-column"
            :elevation="hover ? 12 : 2"
          >
            <v-card-title>Plan Normal</v-card-title>
            <v-card-text>
              <ul>
                <li>4 toneladas de producto escogido cada trimestre</li>
                <li>Hasta 9% de descuento en la tienda online</li>
                <li>Asistencia al cliente normal</li>
              </ul>
            </v-card-text>
            <div class="mt-5 cAction">
              <v-divider class="mx-4 mb-5"></v-divider>
              <strong
                class="text-h4 ms-5 font-weight-bold"
                style="color: var(--v-primary-base)"
              >
                149.99€ / 3 meses
              </strong>
              <br />
              <p class="text-h5 ms-7 font-weight-bold">(57.99 / mes)</p>
            </div>
          </v-card>
        </v-hover>
      </v-col>
      <v-col cols="12" md="4" class="px-5 px-lg-15">
        <v-hover v-slot="{ hover }" >
          <v-card
            style="cursor: pointer"
            height="100%"
            width="100%"
            class="d-flex flex-column"
            :elevation="hover ? 12 : 2"
          >
            <v-card-title>Plan Premium</v-card-title>
            <v-card-text>
              <ul>
                <li>6 toneladas de producto escogido cada trimestre</li>
                <li>Hasta 23% de descuento en la tienda online</li>
                <li>Asistencia al cliente personalizada</li>
              </ul>
            </v-card-text>
            <div class="mt-5 cAction">
              <v-divider class="mx-4 mb-5"></v-divider>
              <strong
                class="text-h4 ms-5 font-weight-bold"
                style="color: var(--v-primary-base)"
              >
                199.99€ / 3 meses
              </strong>
              <br />
              <p class="text-h5 ms-7 font-weight-bold">(73.99 / mes)</p>
            </div>
          </v-card>
        </v-hover>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  name: "FooterComponent",
  data() {
    return {};
  },
};
</script>
