<template>
  <v-app>
    <SearchBar></SearchBar>
  </v-app>

</template>

<script>
import SearchBar from './components/SearchBar';

export default {
  name: 'App',
  components: {
    SearchBar
  },
  data: () => ({
    //
  }),
};
</script>
