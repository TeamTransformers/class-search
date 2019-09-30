<template>
	<v-container fluid>
		<!-- Term Select + Filter Button -->
		<v-row justify="center">
			<v-card width="200">
				<v-card-actions>
					<v-overflow-btn large label="Fall 2019">
					</v-overflow-btn>
				</v-card-actions>
			</v-card>

			<v-divider vertical></v-divider>

			<v-card min-width="300">
				<v-card-actions>
					<v-container>
					<v-btn tile block large v-on="on" target="#filter-menu">Filters</v-btn>
					</v-container>
				</v-card-actions>
			</v-card>
		</v-row>
		
		<!-- Filter Menu -->
		<v-row justify="center">
			<v-card width="500" id="filter-menu">
			<v-card-actions>
				<v-menu>
					<v-btn>TEXT</v-btn>
				</v-menu>
			</v-card-actions>
			</v-card>
		</v-row>
	</v-container>
</template>
