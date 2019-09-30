<template>
  <v-app>

    <Course></Course>

    <SearchBar></SearchBar>

  </v-app>
</template>

<script>

import Course from './components/Course';

import SearchBar from './components/SearchBar';


export default {
  name: 'App',
  components: {

    Course

    SearchBar

  },
  data: () => ({
    //
  }),
};
</script>
