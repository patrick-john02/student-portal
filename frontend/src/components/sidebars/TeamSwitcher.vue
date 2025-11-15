<script setup lang="ts">
import type { Component } from "vue"
import { ref } from "vue"
import {
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
} from "@/components/ui/sidebar"

const props = defineProps<{
  teams: {
    name: string
    logo: Component
    plan: string
  }[]
}>()

const activeTeam = ref(props.teams[0] ?? ({} as typeof props.teams[number]))

</script>

<template>
  <SidebarMenu>
    <SidebarMenuItem>
      <SidebarMenuButton
        size="lg"
        class="flex items-center gap-2"
      >
        <div class="flex aspect-square size-8 items-center justify-center rounded-lg bg-white text-black overflow-hidden">
          <img src="/ucv_logo1.png" alt="Team Logo" class="size-6 object-contain" />
        </div>

        <div class="grid flex-1 text-left text-sm leading-tight">
          <span class="truncate font-semibold">
            {{ activeTeam.name }}
          </span>
          <span class="truncate text-xs">{{ activeTeam.plan }}</span>
        </div>
      </SidebarMenuButton>
    </SidebarMenuItem>
  </SidebarMenu>
</template>
