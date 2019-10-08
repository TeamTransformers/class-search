<template>
<div id="Subject">
  <li v-repeat="display">
    <expansion-panels  multiple>
      <v-expansion-panel>
        <v-expansion-panel-header >{{$value}}</v-expansion-panel-header>

        <v-expansion-panel-content>
          <v-expansion-panels>
            <Course></Course>
            <Course></Course>
          </v-expansion-panels>
        </v-expansion-panel-content>
      </v-expansion-panel>
    </expansion-panels>
  </li>
</div>
</template>


<script>
import Course from "./Course";
export default {
  name: "Subject",
  props: {
    results: {
      type: Array
    }
  },
  components: {
    Course
  },
  data: function() {
    return {
      display: []
    };
  },
  watch: {
    results: function() {
      this.display.push(this.results);
    }
  }
};
</script>
