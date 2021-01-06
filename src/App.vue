<template>
  <v-app>
    <v-app-bar
      app
      dark
      hide-on-scroll
    >
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/NTUST-Emblem.png/220px-NTUST-Emblem.png"
          transition="scale-transition"
          width="40"
        />
       
      </div>

      <v-spacer></v-spacer>

    </v-app-bar>

    <v-main>
      <HelloWorld/>
    </v-main>
  </v-app>
</template>

<script>
import HelloWorld from './components/FilterGallery';

export default {
  name: 'App',

  components: {
    HelloWorld,
  },

  data: () => ({
    //
  }),
};
</script>
