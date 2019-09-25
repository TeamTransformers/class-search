<template>
	<v-card class="overflow-hidden">
		<v-app-bar
			absolute
			color="red darken-3"
			dark
			hide-on-scroll
			scroll-target="#results"
		>
			<v-app-bar-nav-icon></v-app-bar-nav-icon>
			<v-toolbar-title>Filter Bar</v-toolbar-title>
			<div class="flex-grow-1"></div>

		</v-app-bar>

		<v-sheet
			id="results"
			class="overflow-y-auto"
			max-height="600"
		>
			<v-container style="height: 10000px;"></v-container>
		</v-sheet>
	</v-card>
</template>
