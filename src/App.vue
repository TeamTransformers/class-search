<template>
  <v-app>
    <v-expansion-panels>
    <FilterBar></FilterBar>
    </v-expansion-panels>
    <SearchBar></SearchBar>
  </v-app>

</template>

<script>
import FilterBar from './components/FilterBar';
import SectionPage from './components/SectionPage';
import SearchBar from './components/SearchBar';

export default {
  name: 'App',
  components: {
    SearchBar,
    SectionPage,
    FilterBar
  },
  data: () => ({
    //
  }),
  
};
</script>
