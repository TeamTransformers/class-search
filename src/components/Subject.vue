<template>
	<v-expansion-panel>
		<v-expansion-panel-header :value="department_name">{{department_name}}</v-expansion-panel-header>

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
	props:['department_name'],
    components:{
        Course
	},
	data(){
		return{
			department: []
		}
	}
}
</script>
