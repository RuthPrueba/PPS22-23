<template>
  <div>
    <v-breadcrumbs :items="breadcrubms"></v-breadcrumbs>
    <v-row>
      <v-col cols="12">
        <v-card
          class="mx-md-16 mx-5"
          style="border-top: 3px solid var(--v-primary-base);"
        >
          <v-card-title class="justify-center"> BalsCompany </v-card-title>
          <v-card-text class="text-center">
            BalsCompany nació para dar respuesta a las necesidades del sector
            ganadero porcino: calidad de producto y reducción de costes. En
            BalsCompany existe una clara vocación comercial y creemos que la
            calidad de nuestras operaciones es nuestra principal garantía.
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col md="6" cols="12">
        <v-card
          class="ms-md-16 mx-5"
          style="height: 100%; border-top: 3px solid var(--v-primary-base)"
        >
          <v-card-title class="justify-center"> Misión </v-card-title>
          <v-card-text class="text-center">
            Maximizar la satisfacción de nuestros clientes ofreciéndoles
            soluciones acordes a sus necesidades, minimizando el gasto en
            producción y optimizando nuestros recursos. Contribuir al desarrollo
            de nuestros colaboradores con el objetivo de que logren alcanzar
            todo su potencial ofreciéndoles apoyo y formación.
          </v-card-text>
        </v-card>
      </v-col>
      <v-col md="6" cols="12">
        <v-card
          class="me-md-16 mx-5"
          style="height: 100%; border-top: 3px solid var(--v-primary-base)"
        >
          <v-card-title class="justify-center"> Visión </v-card-title>
          <v-card-text class="text-center">
            Convertirnos en una empresa referente en el sector, para llegar a
            ser líderes en el sector ganadero.
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <v-row class="justify-center">
      <v-col class="d-flex justify-center">
        <v-card
          class="mx-md-16 mx-5"
          style="max-width: 1200px; border-top: 3px solid var(--v-primary-base); overflow: hidden;"
        >
          <v-card-title class="justify-center"> Valores </v-card-title>
          <div>
            <table style="border-collapse: collapse">
              <tbody>
                <tr style="background-color: var(--v-error-lighten5);">
                  <td>
                    <div class="d-flex justify-center flex-column align-center">
                      <v-icon color="primary" class="mt-5">
                        mdi-file-search-outline
                      </v-icon>
                      <p class="mx-5 mb-5 text-center font-weight-bold">
                        Transparencia
                      </p>
                    </div>
                  </td>
                  <td>
                    <p class="ma-5">
                      En BalsCompany somos totalmente transparentes en cuanto a
                      información financiera. Disponemos de un equipo que
                      facilitará esa información lo antes posible.
                    </p>
                  </td>
                </tr>
                <tr>
                  <td>
                    <div class="d-flex justify-center flex-column align-center">
                      <v-icon color="primary" class="mt-5">
                        mdi-handshake-outline
                      </v-icon>
                      <p class="mx-5 mb-5 text-center font-weight-bold">
                        Fiabilidad
                      </p>
                    </div>
                  </td>
                  <td>
                    <p class="ma-5">
                      Creemos que la mejor forma de fidelizar al cliente es que él
                      mismo compruebe mes a mes el ahorro en sus gastos.
                    </p>
                  </td>
                </tr>
                <tr style="background-color: var(--v-error-lighten5)">
                  <td>
                    <div class="d-flex justify-center flex-column align-center">
                      <v-icon color="primary" class="mt-5">
                        mdi-account-group-outline
                      </v-icon>
                      <p class="mx-5 mb-5 text-center font-weight-bold">
                        Empleados
                      </p>
                    </div>
                  </td>
                  <td>
                    <p class="ma-5">
                      Creemos que sólo podemos crecer de la mano de nuestros
                      empleados, por lo que les ofrecemos apoyo continuado y
                      herramientas para que puedan desarrollar todo su potencial.
                    </p>
                  </td>
                </tr>
                <tr>
                  <td>
                    <div class="d-flex justify-center flex-column align-center">
                      <v-icon color="primary" class="mt-5">
                        mdi-sprout-outline
                      </v-icon>
                      <p class="mb-0 mx-5 pb-5 text-center font-weight-bold">
                        Sostenibilidad
                      </p>
                    </div>
                  </td>
                  <td>
                    <p class="ma-5">
                      Apuntamos a optimizar nuestro consumo energético y reducir
                      las expulsiones a la atmósfera para minimizar nuestro
                      impacto medioambiental.
                    </p>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  name: "InfoView",
  data() {
    return {
      breadcrubms: [
      {
        text: 'Inicio',
        exact: true,
        to: '/',
      },
      {
        text: 'Info',
        exact: true,
        disabled: true,
        to: '/info',
      },
      ]
    };
  },
};
</script>
