<script lang="ts">
export const description = "General system settings"
export const iframeHeight = "800px"
export const containerClass = "w-full h-full"
</script>

<script setup lang="ts">
import { ref } from "vue"

import AppSidebar from "@/components/sidebars/AppSidebar.vue"
import {
  SidebarProvider,
  SidebarInset,
  SidebarTrigger,
} from "@/components/ui/sidebar"

import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbList,
  BreadcrumbLink,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "@/components/ui/breadcrumb"

import { Separator } from "@/components/ui/separator"

import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardContent,
} from "@/components/ui/card"

import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Switch } from "@/components/ui/switch"
import { Label } from "@/components/ui/label"
import { Select, SelectTrigger, SelectValue, SelectContent, SelectItem } from "@/components/ui/select"

import { Save, Globe, Bell } from "lucide-vue-next"

const userRole = "Admin"

// Dummy form state
const systemName = ref("UCV Senior High Portal")
const academicYear = ref("2024-2025")
const timezone = ref("Asia/Manila")

const enableNotifications = ref(true)
const maintenanceMode = ref(false)
</script>

<template>
  <SidebarProvider>
    <AppSidebar :userRole="userRole" />

    <SidebarInset>
      <!-- Header -->
      <header class="flex h-16 items-center gap-2 px-4 transition-all">
        <SidebarTrigger class="-ml-2" />
        <Separator orientation="vertical" class="mx-2 h-4" />

        <Breadcrumb>
          <BreadcrumbList>
            <BreadcrumbItem>
              <BreadcrumbLink href="/admin/dashboard">Admin</BreadcrumbLink>
            </BreadcrumbItem>
            <BreadcrumbSeparator />
            <BreadcrumbItem>
              <BreadcrumbPage>General Settings</BreadcrumbPage>
            </BreadcrumbItem>
          </BreadcrumbList>
        </Breadcrumb>
      </header>

      <!-- Page Content -->
      <div class="flex flex-1 flex-col gap-4 p-4 pt-0">

        <!-- Page Title -->
        <div>
          <h2 class="text-2xl font-bold tracking-tight">General Settings</h2>
          <p class="text-sm text-muted-foreground">
            Configure system preferences and core application settings.
          </p>
        </div>

        <div class="grid gap-4 md:grid-cols-2">
          
          <!-- System Information -->
          <Card>
            <CardHeader>
              <CardTitle>System Information</CardTitle>
              <CardDescription>
                Update system name and academic year settings.
              </CardDescription>
            </CardHeader>

            <CardContent class="space-y-4">
              <div class="space-y-1">
                <Label>System Name</Label>
                <Input v-model="systemName" placeholder="System Name" />
              </div>

              <div class="space-y-1">
                <Label>Active Academic Year</Label>
                <Select v-model="academicYear">
                  <SelectTrigger>
                    <SelectValue placeholder="Select Academic Year" />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="2023-2024">2023-2024</SelectItem>
                    <SelectItem value="2024-2025">2024-2025</SelectItem>
                    <SelectItem value="2025-2026">2025-2026</SelectItem>
                  </SelectContent>
                </Select>
              </div>

              <Button class="flex items-center gap-2 mt-2">
                <Save class="h-4 w-4" /> Save Changes
              </Button>
            </CardContent>
          </Card>

          <!-- System Preferences -->
          <Card>
            <CardHeader>
              <CardTitle>System Preferences</CardTitle>
              <CardDescription>
                Manage timezone, notifications, and maintenance mode.
              </CardDescription>
            </CardHeader>

            <CardContent class="space-y-4">

              <div class="space-y-1">
                <Label>Timezone</Label>
                <Select v-model="timezone">
                  <SelectTrigger>
                    <SelectValue placeholder="Select Timezone" />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="Asia/Manila">Asia/Manila</SelectItem>
                    <SelectItem value="Asia/Singapore">Asia/Singapore</SelectItem>
                    <SelectItem value="UTC">UTC</SelectItem>
                  </SelectContent>
                </Select>
              </div>

              <div class="flex items-center justify-between py-2">
                <div class="flex items-center gap-2">
                  <Bell class="h-4 w-4 text-muted-foreground" />
                  <Label>Enable Notifications</Label>
                </div>
                <Switch v-model:checked="enableNotifications" />
              </div>

              <div class="flex items-center justify-between py-2">
                <div class="flex items-center gap-2">
                  <Globe class="h-4 w-4 text-muted-foreground" />
                  <Label>Maintenance Mode</Label>
                </div>
                <Switch v-model:checked="maintenanceMode" />
              </div>

              <Button class="flex items-center gap-2 mt-2">
                <Save class="h-4 w-4" /> Apply Settings
              </Button>

            </CardContent>
          </Card>

        </div>
      </div>
    </SidebarInset>
  </SidebarProvider>
</template>
