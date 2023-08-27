<script lang="ts">
	import { VisXYContainer, VisLine, VisAxis } from '@unovis/svelte';

	type DataRecord = { x: number; y: number };
	const data: DataRecord[] = [
		{ x: 0, y: 0 },
		{ x: 1, y: 2 },
		{ x: 2, y: 1 }
	];
</script>

<h1 class="text-4xl tracking-tighter font-bold">UnoVis</h1>

<VisXYContainer height={600} {data}>
	<VisLine {data} x={(d) => d.x} y={(d) => d.y} />
	<VisAxis type="x" />
	<VisAxis type="y" />
</VisXYContainer>
