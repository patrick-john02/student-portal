<script lang="ts">
export const description = "Teacher schedules page"
export const iframeHeight = "800px"
export const containerClass = "w-full h-full"
</script>

<script setup lang="ts">
import AppSidebar from "@/components/sidebars/AppSidebar.vue"
import {
  SidebarProvider,
  SidebarInset,
  SidebarTrigger,
} from "@/components/ui/sidebar"

import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbList,
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

import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"
import { Calendar, Clock, BookOpen } from "lucide-vue-next"

const userRole = "Teacher"

// Dummy weekly schedule
const schedule = [
  {
    day: "Monday",
    classes: [
      { subject: "General Mathematics", section: "STEM 11-A", time: "8:00 AM - 9:30 AM", color: "bg-blue-500" },
      { subject: "Earth & Life Science", section: "STEM 11-B", time: "10:00 AM - 11:30 AM", color: "bg-green-500" },
    ],
  },
  {
    day: "Tuesday",
    classes: [
      { subject: "Oral Communication", section: "HUMSS 11-A", time: "9:00 AM - 10:30 AM", color: "bg-yellow-500" },
      { subject: "Physical Education", section: "GAS 12-B", time: "1:00 PM - 2:30 PM", color: "bg-red-500" },
    ],
  },
  {
    day: "Wednesday",
    classes: [
      { subject: "General Mathematics", section: "STEM 11-A", time: "8:00 AM - 9:30 AM", color: "bg-blue-500" },
    ],
  },
  {
    day: "Thursday",
    classes: [
      { subject: "Earth & Life Science", section: "STEM 11-B", time: "10:00 AM - 11:30 AM", color: "bg-green-500" },
      { subject: "Physical Education", section: "GAS 12-B", time: "1:00 PM - 2:30 PM", color: "bg-red-500" },
    ],
  },
  {
    day: "Friday",
    classes: [
      { subject: "Oral Communication", section: "HUMSS 11-A", time: "9:00 AM - 10:30 AM", color: "bg-yellow-500" },
    ],
  },
]
</script>

<template>
  <SidebarProvider>
    <AppSidebar :userRole="userRole" />

    <SidebarInset>
      <!-- Header -->
      <header class="flex h-16 shrink-0 items-center gap-2 px-4 transition-all">
        <SidebarTrigger class="-ml-1" />
        <Separator orientation="vertical" class="mx-2 h-4" />

        <Breadcrumb>
          <BreadcrumbList>
            <BreadcrumbItem>
              <BreadcrumbLink href="/teacher/dashboard">Teacher</BreadcrumbLink>
            </BreadcrumbItem>
            <BreadcrumbSeparator />
            <BreadcrumbItem>
              <BreadcrumbPage>Schedules</BreadcrumbPage>
            </BreadcrumbItem>
          </BreadcrumbList>
        </Breadcrumb>
      </header>

      <!-- Content -->
      <div class="flex flex-1 flex-col gap-4 p-4 pt-0">

        <!-- Page Header -->
        <div class="flex items-center justify-between">
          <div>
            <h2 class="text-2xl font-bold tracking-tight">My Class Schedule</h2>
            <p class="text-sm text-muted-foreground">
              View your weekly class schedule and teaching assignments.
            </p>
          </div>

          <Button class="flex items-center gap-2">
            <Calendar class="h-4 w-4" />
            Export Schedule
          </Button>
        </div>

        <!-- Weekly Schedule -->
        <Card>
          <CardHeader>
            <CardTitle>Weekly Overview</CardTitle>
            <CardDescription>Your complete teaching schedule for the week.</CardDescription>
          </CardHeader>

          <CardContent>
            <div class="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
              <!-- Day Card -->
              <div
                v-for="day in schedule"
                :key="day.day"
                class="rounded-lg border p-4 space-y-3 hover:bg-muted/30 transition"
              >
                <h3 class="font-semibold text-lg flex items-center gap-2">
                  <Calendar class="h-4 w-4 text-primary" />
                  {{ day.day }}
                </h3>

                <div v-if="day.classes.length > 0" class="space-y-3">
                  <div
                    v-for="cls in day.classes"
                    :key="cls.subject + cls.time"
                    class="rounded-md border p-3 bg-card hover:bg-accent transition cursor-pointer"
                  >
                    <div class="flex items-start justify-between">
                      <p class="font-medium text-sm flex items-center gap-2">
                        <span class="h-2 w-2 rounded-full" :class="cls.color"></span>
                        {{ cls.subject }}
                      </p>
                      <Badge variant="secondary">{{ cls.section }}</Badge>
                    </div>

                    <div class="flex items-center gap-2 mt-2 text-xs text-muted-foreground">
                      <Clock class="h-3 w-3" />
                      {{ cls.time }}
                    </div>
                  </div>
                </div>

                <p v-else class="text-sm text-muted-foreground italic">
                  No classes scheduled.
                </p>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>
    </SidebarInset>
  </SidebarProvider>
</template>
