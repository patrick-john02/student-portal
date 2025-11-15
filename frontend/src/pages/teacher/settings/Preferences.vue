<script lang="ts">
export const description = "Teacher preferences settings page"
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
  BreadcrumbList,
  BreadcrumbItem,
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
  CardFooter,
} from "@/components/ui/card"

import { Button } from "@/components/ui/button"
import { Label } from "@/components/ui/label"
import { Input } from "@/components/ui/input"
import {
  Select,
  SelectTrigger,
  SelectValue,
  SelectContent,
  SelectItem,
} from "@/components/ui/select"

import { Switch } from "@/components/ui/switch"

import {
  Sun,
  Moon,
  Bell,
  Volume2,
  Languages,
  Check,
  NotebookPen,
} from "lucide-vue-next"

const userRole = "Teacher"

// Preferences states
const darkMode = ref(false)
const notifications = ref(true)
const soundEnabled = ref(true)
const language = ref("English")
const defaultSection = ref("STEM 11 - A")
</script>

<template>
  <SidebarProvider>
    <AppSidebar :userRole="userRole" />

    <SidebarInset>
      <!-- Header -->
      <header class="flex h-16 shrink-0 items-center gap-2 px-4">
        <SidebarTrigger class="-ml-1" />
        <Separator orientation="vertical" class="mx-2 h-4" />

        <Breadcrumb>
          <BreadcrumbList>
            <BreadcrumbItem>
              <BreadcrumbLink href="/teacher/dashboard">Teacher</BreadcrumbLink>
            </BreadcrumbItem>
            <BreadcrumbSeparator />
            <BreadcrumbItem>
              <BreadcrumbPage>Preferences</BreadcrumbPage>
            </BreadcrumbItem>
          </BreadcrumbList>
        </Breadcrumb>
      </header>

      <!-- CONTENT -->
      <div class="p-4 flex flex-col gap-6 pb-12">
        <h2 class="text-2xl font-bold tracking-tight">Preferences</h2>
        <p class="text-sm text-muted-foreground">
          Customize your interface, notifications, and language settings.
        </p>

        <!-- THEME SETTINGS -->
        <Card>
          <CardHeader>
            <CardTitle>Appearance</CardTitle>
            <CardDescription>Set your theme and visual preferences.</CardDescription>
          </CardHeader>

          <CardContent class="space-y-6">
            <!-- DARK MODE -->
            <div class="flex items-center justify-between">
              <div>
                <p class="font-medium flex items-center gap-2">
                  <Moon class="h-4 w-4" />
                  Dark Mode
                </p>
                <p class="text-sm text-muted-foreground">
                  Switch between light and dark themes.
                </p>
              </div>
              <Switch v-model:checked="darkMode" />
            </div>

            <!-- LANGUAGE -->
            <div class="grid gap-2">
              <Label class="flex items-center gap-2">
                <Languages class="h-4 w-4" />
                Language
              </Label>
              <Select v-model="language">
                <SelectTrigger>
                  <SelectValue placeholder="Select language" />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="English">English</SelectItem>
                  <SelectItem value="Filipino">Filipino</SelectItem>
                </SelectContent>
              </Select>
            </div>
          </CardContent>

          <CardFooter class="flex justify-end">
            <Button>Save Appearance</Button>
          </CardFooter>
        </Card>

        <!-- NOTIFICATION SETTINGS -->
        <Card>
          <CardHeader>
            <CardTitle>Notifications</CardTitle>
            <CardDescription>Manage app alerts and message preferences.</CardDescription>
          </CardHeader>

          <CardContent class="space-y-6">
            <!-- Enable Notifications -->
            <div class="flex items-center justify-between">
              <div>
                <p class="font-medium flex items-center gap-2">
                  <Bell class="h-4 w-4" />
                  Enable Notifications
                </p>
                <p class="text-sm text-muted-foreground">
                  Receive alerts for assignments, messages, and updates.
                </p>
              </div>
              <Switch v-model:checked="notifications" />
            </div>

            <!-- Sound -->
            <div class="flex items-center justify-between">
              <div>
                <p class="font-medium flex items-center gap-2">
                  <Volume2 class="h-4 w-4" />
                  Sound
                </p>
                <p class="text-sm text-muted-foreground">
                  Play sound when receiving messages.
                </p>
              </div>
              <Switch v-model:checked="soundEnabled" />
            </div>
          </CardContent>

          <CardFooter class="flex justify-end">
            <Button>Save Notification Settings</Button>
          </CardFooter>
        </Card>

        <!-- CLASSROOM PREFERENCES -->
        <Card>
          <CardHeader>
            <CardTitle>Classroom Preferences</CardTitle>
            <CardDescription>
              Set your default classroom options.
            </CardDescription>
          </CardHeader>

          <CardContent class="space-y-6">
            <!-- DEFAULT SECTION -->
            <div class="grid gap-2">
              <Label class="flex items-center gap-2">
                <NotebookPen class="h-4 w-4" />
                Default Section
              </Label>
              <Select v-model="defaultSection">
                <SelectTrigger>
                  <SelectValue placeholder="Select default section" />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="STEM 11 - A">STEM 11 - A</SelectItem>
                  <SelectItem value="ABM 12 - A">ABM 12 - A</SelectItem>
                  <SelectItem value="HUMSS 12 - B">HUMSS 12 - B</SelectItem>
                </SelectContent>
              </Select>
            </div>
          </CardContent>

          <CardFooter class="flex justify-end">
            <Button>Save Classroom Preferences</Button>
          </CardFooter>
        </Card>
      </div>
    </SidebarInset>
  </SidebarProvider>
</template>
