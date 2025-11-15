<script setup lang="ts">
import type { SidebarProps } from "@/components/ui/sidebar"
import { useSidebarData, type UserRole } from "@/composables/useSidebarData"
import NavMain from "@/components/sidebars/NavMain.vue"
import NavProjects from "@/components/sidebars/NavProjects.vue"
import NavUser from "@/components/sidebars/NavUser.vue"
import TeamSwitcher from "@/components/sidebars/TeamSwitcher.vue"

import {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarHeader,
  SidebarRail,
} from "@/components/ui/sidebar"

interface Props extends SidebarProps {
  userRole: UserRole
}

const props = withDefaults(defineProps<Props>(), {
  collapsible: "icon",
  userRole: "Student",
})

const { sidebarData } = useSidebarData(props.userRole)
</script>

<template>
  <Sidebar v-bind="props">
    <SidebarHeader>
      <TeamSwitcher :teams="sidebarData.teams" />
    </SidebarHeader>
    <SidebarContent>
      <NavMain :items="sidebarData.navMain" />
      <NavProjects :projects="sidebarData.projects" />
    </SidebarContent>
    <SidebarFooter>
      <NavUser :user="sidebarData.user" />
    </SidebarFooter>
    <SidebarRail />
  </Sidebar>
</template>