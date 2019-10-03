<template>
  <v-app>
	<v-container>
	<SearchBar/>
	<v-expansion-panels>
		<FilterBar/>
		<Subject/>
		<Subject/>
	</v-expansion-panels>
	</v-container>
  </v-app>

</template>

<script>
import Course from './components/Course';
import SearchBar from './components/SearchBar';
import FilterBar from './components/FilterBar';
import SectionPage from './components/SectionPage';
import Subject from './components/Subject';

export default {
  name: 'App',
  components: {
	Course,
	FilterBar,
    SearchBar,
	SectionPage,
	Subject
  },
  data: () => ({
    //
  }),
};
</script>
