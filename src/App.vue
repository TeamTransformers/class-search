<template>
  <v-app>
    <v-content>
      <SectionPage/>
    </v-content>
  </v-app>

</template>

<script>
import HelloWorld from './components/HelloWorld';
import SectionPage from './components/SectionPage';


export default {
  name: 'App',
  components: {
    HelloWorld,
    SectionPage,

  },
  data: () => ({
    //
  }),
};
</script>
