<template>
  <v-app>
    <Test></Test>
  </v-app>

</template>

<script>
import FilterBar from './components/FilterBar';
import SectionPage from './components/SectionPage';
import SearchBar from './components/SearchBar';
import Test from './components/Test';
export default {
  name: 'App',
  components: {
    SearchBar,
    SectionPage,
    FilterBar,
    Test
  },
  data: () => ({
    //
  }),
};
</script>
