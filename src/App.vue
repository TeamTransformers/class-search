<template>
  <v-container >
    <div v-show="display">
    <SearchBar :result="searchResults" @searchArrayFilter="searchResults=$event"></SearchBar>
    <v-expansion-panels>
      <FilterBar />
      <Subject
        :result="display"
        @displaySec="display=false"
        v-for="department in searchResults"
        :key="department.id"
        :department_name="department"
      ></Subject>
    </v-expansion-panels>
    </div>
    <div v-show="!display">
      <SectionPage/>
    </div>
  </v-container>
</template>

<script>
import Course from "./components/Course";
import SearchBar from "./components/SearchBar";
import FilterBar from "./components/FilterBar";
import SectionPage from "./components/SectionPage";
import Subject from "./components/Subject";

export default {
  name: "App",
  components: {
    Course,
    FilterBar,
    SearchBar,
    SectionPage,
    Subject
  },
  data() {
    return {
      display: true,
      searchResults: []
    };
  }
};
</script>
