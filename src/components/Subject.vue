<template>
	<v-expansion-panel>
		<v-expansion-panel-header :value="department_name" class="red darken-3">{{department_name}}</v-expansion-panel-header>
        <v-expansion-panel-content>
          <v-expansion-panels>
            <Course @next="send"></Course>
            <Course @next="send"></Course>
          </v-expansion-panels>
        </v-expansion-panel-content>
      </v-expansion-panel>
</template>


<script>
import Course from "./Course";
export default {
	props:['department_name'],
    components:{
        Course
	},
	data(){
		return{
			department: []
		}
  },
  methods:{
        send(){
            this.$emit('final');
        }
  },
}
</script>
