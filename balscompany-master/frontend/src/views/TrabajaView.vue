<template>
    <div>
        
      <v-breadcrumbs
        large
        :items="[
          { text: 'Inicio', to: '/', exact: true },
          { text: 'Trabaja con nosotros', disabled: true, exact: true },
        ]"
      ></v-breadcrumbs>
      <v-breadcrumbs :items="breadcrubms"></v-breadcrumbs>
      <v-row style="max-width: 700px;" class="mx-auto mb-3 align-center justify-space-around">
        <v-col cols="12">
          <v-card class="pb-5" style="border-top: 3px solid var(--v-primary-base);">
            <v-card-title>¿Quieres trabajar con nosotros?</v-card-title>
            <v-card-text>
              <p>
                En BalsCompany creemos que sólo podemos crecer de la mano de nuestros empleados, por lo que les ofrecemos apoyo continuado y herramientas para que puedan desarrollar todo su potencial.
              </p>
              <p>Envíenos su CV rellenando este simple formulario:</p>
            </v-card-text>
            <v-form ref="form" class="mx-5">
              <v-text-field
                label="Nombre*"
                outlined
                prepend-icon="mdi-card-account-details"
                :rules="nombre"
                value=""
              ></v-text-field>
              <v-text-field
                label="Email*"
                outlined
                prepend-icon="mdi-at"
                :rules="email"
                value=""
              ></v-text-field>
              <v-file-input
                truncate-length="15"
                outlined
                label="CV*"
                :rules="cv"
              ></v-file-input>
              <v-textarea
                outlined
                name="input-7-4"
                label="Mensaje"
                prepend-icon="mdi-message"
              ></v-textarea>
              <v-btn color="primary" @click="enviar" class="ms-8"> Enviar </v-btn>
              <br />
              <br />
              <text class="ms-8"> * Campos obligatorios </text>
            </v-form>
          </v-card>
        </v-col>
      </v-row>
    </div>
  </template>
  
  <script>
  import { validaNombre, validaEmail } from "@/utils/rules.js";
  
  export default {
    name: "AhorraView",
    data() {
      return {
        nombre: [(v) => validaNombre(v)],
        email: [(v) => validaEmail(v)],
        cv: [
          (v) => !!v || "Adjunta tu CV",
          (v) => (v && v.size > 0) || "Adjunta tu CV",
        ],
      };
    },
    methods: {
      async enviar() {
        if (!this.$refs.form.validate()) return;
        else {
          alert("Todo bien, eliminar alert en el despliegue");
        }
      },
    },
  };
  </script>