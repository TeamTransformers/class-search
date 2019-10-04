<template>
	<v-expansion-panel>
		<v-expansion-panel-header>Subject Name</v-expansion-panel-header>

		<v-expansion-panel-content>
			<v-expansion-panels>
				<Course></Course>
				<Course></Course>
			</v-expansion-panels>
		</v-expansion-panel-content>
	</v-expansion-panel>
</template>


<script>
import Course from './Course';
export default {
    components:{
        Course
    }
}
</script>
