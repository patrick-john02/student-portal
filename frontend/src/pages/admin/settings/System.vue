<script lang="ts">
export const description = "System configuration settings"
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

import {
  Select,
  SelectTrigger,
  SelectValue,
  SelectContent,
  SelectItem,
} from "@/components/ui/select"

import {
  ServerCog,
  HardDrive,
  Database,
  Network,
  Save,
  Wrench,
} from "lucide-vue-next"

const userRole = "Admin"

// Dummy configuration values
const apiUrl = ref("https://api.ucv.edu/v1")
const storagePath = ref("/var/ucv/storage")
const backupFrequency = ref("daily")
const autoBackup = ref(true)
const errorTracking = ref(true)
const debugMode = ref(false)
</script>

<template>
  <SidebarProvider>
    <AppSidebar :userRole="userRole" />

    <SidebarInset>
      <!-- Page Header -->
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
              <BreadcrumbPage>System Settings</BreadcrumbPage>
            </BreadcrumbItem>
          </BreadcrumbList>
        </Breadcrumb>
      </header>

      <!-- Main Content -->
      <div class="flex flex-1 flex-col gap-4 p-4 pt-0">

        <div>
          <h2 class="text-2xl font-bold tracking-tight">System Settings</h2>
          <p class="text-sm text-muted-foreground">
            Manage backend services, API endpoints, and system behaviors.
          </p>
        </div>

        <div class="grid gap-4 md:grid-cols-2">

          <!-- API Configuration -->
          <Card>
            <CardHeader>
              <CardTitle class="flex items-center gap-2">
                <ServerCog class="h-4 w-4" />
                API Configuration
              </CardTitle>
              <CardDescription>
                Configure API routes, endpoints, and service URLs.
              </CardDescription>
            </CardHeader>

            <CardContent class="space-y-4">
              <div class="space-y-1">
                <Label>API Base URL</Label>
                <Input v-model="apiUrl" placeholder="https://api.example.com" />
              </div>

              <div class="space-y-1">
                <Label>Backup Frequency</Label>
                <Select v-model="backupFrequency">
                  <SelectTrigger>
                    <SelectValue placeholder="Select Frequency" />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="daily">Daily</SelectItem>
                    <SelectItem value="weekly">Weekly</SelectItem>
                    <SelectItem value="monthly">Monthly</SelectItem>
                  </SelectContent>
                </Select>
              </div>

              <Button class="flex items-center gap-2 mt-2">
                <Save class="h-4 w-4" />
                Save Changes
              </Button>
            </CardContent>
          </Card>

          <!-- Storage & Backup -->
          <Card>
            <CardHeader>
              <CardTitle class="flex items-center gap-2">
                <HardDrive class="h-4 w-4" />
                Storage & Backups
              </CardTitle>
              <CardDescription>
                Manage local storage paths and backup automation.
              </CardDescription>
            </CardHeader>

            <CardContent class="space-y-4">
              <div class="space-y-1">
                <Label>Storage Directory</Label>
                <Input v-model="storagePath" placeholder="/var/storage/..." />
              </div>

              <div class="flex items-center justify-between py-2">
                <div class="flex items-center gap-2">
                  <Database class="h-4 w-4 text-muted-foreground" />
                  <Label>Enable Auto Backup</Label>
                </div>
                <Switch v-model:checked="autoBackup" />
              </div>

              <Button class="flex items-center gap-2 mt-2">
                <Save class="h-4 w-4" />
                Update Storage Settings
              </Button>
            </CardContent>
          </Card>

          <!-- Error Tracking -->
          <Card>
            <CardHeader>
              <CardTitle class="flex items-center gap-2">
                <Network class="h-4 w-4" />
                Error & Monitoring
              </CardTitle>
              <CardDescription>
                Enable system monitoring and debugging tools.
              </CardDescription>
            </CardHeader>

            <CardContent class="space-y-4">
              <div class="flex items-center justify-between">
                <div class="flex items-center gap-2">
                  <Wrench class="h-4 w-4 text-muted-foreground" />
                  <Label>Error Tracking</Label>
                </div>
                <Switch v-model:checked="errorTracking" />
              </div>

              <div class="flex items-center justify-between">
                <div class="flex items-center gap-2">
                  <Wrench class="h-4 w-4 text-muted-foreground" />
                  <Label>Debug Mode</Label>
                </div>
                <Switch v-model:checked="debugMode" />
              </div>

              <Button class="flex items-center gap-2 mt-2">
                <Save class="h-4 w-4" />
                Apply Changes
              </Button>
            </CardContent>
          </Card>

        </div>
      </div>
    </SidebarInset>
  </SidebarProvider>
</template>
