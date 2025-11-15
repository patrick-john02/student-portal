<script lang="ts">
export const description = "Teacher consultations page"
export const iframeHeight = "800px"
export const containerClass = "w-full h-full"
</script>

<script setup lang="ts">
import { ref, computed } from "vue"

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
} from "@/components/ui/card"

import { Button } from "@/components/ui/button"
import { Badge } from "@/components/ui/badge"
import { Input } from "@/components/ui/input"
import {
  Select,
  SelectTrigger,
  SelectContent,
  SelectItem,
  SelectValue,
} from "@/components/ui/select"

import {
  Table,
  TableHeader,
  TableRow,
  TableHead,
  TableBody,
  TableCell,
} from "@/components/ui/table"

import {
  MessageSquare,
  CalendarDays,
  ClipboardCheck,
  User,
  Clock4,
} from "lucide-vue-next"

const userRole = "Teacher"

// Filters
const statusFilter = ref("")
const sectionFilter = ref("")
const search = ref("")

// Dummy consultations data
const consultations = ref([
  {
    id: 1,
    student: "Samantha Cruz",
    section: "STEM 11 - A",
    topic: "Performance feedback",
    schedule: "2025-02-18 10:00 AM",
    status: "Scheduled",
  },
  {
    id: 2,
    student: "Joshua Ramirez",
    section: "ABM 12 - A",
    topic: "Grade concerns",
    schedule: "2025-02-17 2:00 PM",
    status: "Completed",
  },
  {
    id: 3,
    student: "Marjorie Tan",
    section: "HUMSS 12 - B",
    topic: "Absence clarification",
    schedule: "2025-02-20 11:30 AM",
    status: "Pending",
  },
])

const filteredConsultations = computed(() => {
  return consultations.value.filter((c) => {
    const matchStatus = statusFilter.value ? c.status === statusFilter.value : true
    const matchSection = sectionFilter.value ? c.section === sectionFilter.value : true
    const matchSearch = search.value
      ? c.student.toLowerCase().includes(search.value.toLowerCase()) ||
        c.topic.toLowerCase().includes(search.value.toLowerCase())
      : true

    return matchStatus && matchSection && matchSearch
  })
})
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
              <BreadcrumbLink href="/teacher/dashboard">
                Teacher
              </BreadcrumbLink>
            </BreadcrumbItem>
            <BreadcrumbSeparator />
            <BreadcrumbItem>
              <BreadcrumbPage>Consultations</BreadcrumbPage>
            </BreadcrumbItem>
          </BreadcrumbList>
        </Breadcrumb>
      </header>

      <!-- Content -->
      <div class="flex flex-1 flex-col gap-4 p-4 pt-0">
        <!-- Page Title -->
        <div>
          <h2 class="text-2xl font-bold tracking-tight">Student Consultations</h2>
          <p class="text-sm text-muted-foreground">
            Review consultation requests and scheduled meetings.
          </p>
        </div>

        <!-- Summary Cards -->
        <div class="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
          <Card class="border-l-4 border-l-blue-500">
            <CardHeader class="flex flex-row items-center justify-between pb-2">
              <CardTitle class="text-sm font-medium">Scheduled</CardTitle>
              <CalendarDays class="h-5 w-5 text-blue-500" />
            </CardHeader>
            <CardContent>
              <p class="text-2xl font-bold">
                {{ consultations.filter((c) => c.status === "Scheduled").length }}
              </p>
              <p class="text-xs text-muted-foreground mt-1">Upcoming consultations</p>
            </CardContent>
          </Card>

          <Card class="border-l-4 border-l-yellow-500">
            <CardHeader class="flex flex-row items-center justify-between pb-2">
              <CardTitle class="text-sm font-medium">Pending</CardTitle>
              <Clock4 class="h-5 w-5 text-yellow-500" />
            </CardHeader>
            <CardContent>
              <p class="text-2xl font-bold">
                {{ consultations.filter((c) => c.status === "Pending").length }}
              </p>
              <p class="text-xs text-muted-foreground mt-1">Awaiting response</p>
            </CardContent>
          </Card>

          <Card class="border-l-4 border-l-green-500">
            <CardHeader class="flex flex-row items-center justify-between pb-2">
              <CardTitle class="text-sm font-medium">Completed</CardTitle>
              <ClipboardCheck class="h-5 w-5 text-green-500" />
            </CardHeader>
            <CardContent>
              <p class="text-2xl font-bold">
                {{ consultations.filter((c) => c.status === "Completed").length }}
              </p>
              <p class="text-xs text-muted-foreground mt-1">Finished sessions</p>
            </CardContent>
          </Card>
        </div>

        <!-- Filters -->
        <Card>
          <CardHeader>
            <CardTitle>Filters</CardTitle>
            <CardDescription>
              Sort consultations by status, section, or keyword.
            </CardDescription>
          </CardHeader>

          <CardContent>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
              <!-- Status -->
              <Select v-model="statusFilter">
                <SelectTrigger>
                  <SelectValue placeholder="Select Status" />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="Scheduled">Scheduled</SelectItem>
                  <SelectItem value="Pending">Pending</SelectItem>
                  <SelectItem value="Completed">Completed</SelectItem>
                </SelectContent>
              </Select>

              <!-- Section -->
              <Select v-model="sectionFilter">
                <SelectTrigger>
                  <SelectValue placeholder="Select Section" />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="STEM 11 - A">STEM 11 - A</SelectItem>
                  <SelectItem value="ABM 12 - A">ABM 12 - A</SelectItem>
                  <SelectItem value="HUMSS 12 - B">HUMSS 12 - B</SelectItem>
                </SelectContent>
              </Select>

              <!-- Search -->
              <Input v-model="search" placeholder="Search student or topic..." />
            </div>
          </CardContent>
        </Card>

        <!-- Consultations Table -->
        <Card>
          <CardHeader>
            <CardTitle>Consultation Requests</CardTitle>
            <CardDescription>
              View consultation topics, schedules, and statuses.
            </CardDescription>
          </CardHeader>

          <CardContent>
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead>Student</TableHead>
                  <TableHead>Section</TableHead>
                  <TableHead>Topic</TableHead>
                  <TableHead class="text-center">Schedule</TableHead>
                  <TableHead class="text-center">Status</TableHead>
                </TableRow>
              </TableHeader>

              <TableBody>
                <TableRow
                  v-for="c in filteredConsultations"
                  :key="c.id"
                  class="hover:bg-muted/50 cursor-pointer"
                >
                  <TableCell class="font-medium">
                    {{ c.student }}
                  </TableCell>

                  <TableCell>{{ c.section }}</TableCell>
                  <TableCell>{{ c.topic }}</TableCell>

                  <TableCell class="text-center">{{ c.schedule }}</TableCell>

                  <TableCell class="text-center">
                    <Badge
                      :variant="
                        c.status === 'Scheduled'
                          ? 'default'
                          : c.status === 'Pending'
                          ? 'secondary'
                          : 'outline'
                      "
                    >
                      {{ c.status }}
                    </Badge>
                  </TableCell>
                </TableRow>
              </TableBody>
            </Table>
          </CardContent>
        </Card>
      </div>
    </SidebarInset>
  </SidebarProvider>
</template>
