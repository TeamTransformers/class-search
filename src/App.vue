<template>
  <v-container>
    <div v-show="!display">
    <SearchBar :result="searchResults" @searchArrayFilter="searchResults=$event"></SearchBar>
    <v-expansion-panels accordion>
      <FilterBar />
      <Subject
        @final="switchDisplay"
        v-for="department in searchResults"
          :key="department.id"
          :department_name="department"
      ></Subject>
    </v-expansion-panels>
    </div>
    <div v-show="display">
      <SectionPage @restore="switchDisplay"/>
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
    Subject,
  },
  data() {
    return {
      hide:0,
      display: 0,
      searchResults: []
    };
  },
  methods:{
    switchDisplay(){
      if(this.display == 1){
        this.display = 0
      }
      else{
        this.display = 1
      }
    }
  }
};
</script>
